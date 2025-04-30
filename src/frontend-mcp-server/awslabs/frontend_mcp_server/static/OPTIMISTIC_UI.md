# Optimistic UI with React Query and Zustand

## Core Concepts

### What is Optimistic UI?

Optimistic UI is a pattern where the interface updates immediately in response to user actions, before server confirmation. This creates a more responsive user experience by showing the expected result while the actual operation happens in the background.

### Key Benefits

- Improved perceived performance
- Better user experience
- Instant feedback
- Graceful error handling with automatic rollback

## Implementation Guide

### 1. Setup Dependencies

```bash
npm install @tanstack/react-query @tanstack/react-query-devtools zustand
```

### 2. Configure React Query

```typescript
// src/main.tsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  </React.StrictMode>
);
```

### 3. Create Zustand Store

```typescript
// src/store/items.ts
import { create } from 'zustand';

interface Item {
  id: string;
  title: string;
  completed: boolean;
}

interface ItemsStore {
  items: Item[];
  setItems: (items: Item[]) => void;
  addItem: (item: Item) => void;
  updateItem: (id: string, updates: Partial<Item>) => void;
  removeItem: (id: string) => void;
}

export const useItemsStore = create<ItemsStore>((set) => ({
  items: [],
  setItems: (items) => set({ items }),
  addItem: (item) => set((state) => ({
    items: [...state.items, item]
  })),
  updateItem: (id, updates) => set((state) => ({
    items: state.items.map((item) =>
      item.id === id ? { ...item, ...updates } : item
    ),
  })),
  removeItem: (id) => set((state) => ({
    items: state.items.filter((item) => item.id !== id),
  })),
}));
```

### 4. Implement Optimistic Updates

```typescript
// src/hooks/useItems.ts
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { useItemsStore } from '../store/items';

export function useItems() {
  const queryClient = useQueryClient();
  const { setItems, addItem, updateItem, removeItem } = useItemsStore();

  // Fetch items
  const { data: items } = useQuery({
    queryKey: ['items'],
    queryFn: async () => {
      const response = await fetch('/api/items');
      const items = await response.json();
      setItems(items);
      return items;
    },
  });

  // Create item with optimistic update
  const createMutation = useMutation({
    mutationFn: async (newItem: Omit<Item, 'id'>) => {
      const response = await fetch('/api/items', {
        method: 'POST',
        body: JSON.stringify(newItem),
      });
      return response.json();
    },
    onMutate: async (newItem) => {
      // Cancel outgoing refetches
      await queryClient.cancelQueries({ queryKey: ['items'] });

      // Create optimistic item
      const optimisticItem = {
        id: Date.now().toString(),
        ...newItem,
      };

      // Add to store
      addItem(optimisticItem);

      return { optimisticItem };
    },
    onError: (err, newItem, context) => {
      // On error, remove optimistic item
      if (context?.optimisticItem) {
        removeItem(context.optimisticItem.id);
      }
    },
    onSettled: () => {
      // Refetch to sync with server
      queryClient.invalidateQueries({ queryKey: ['items'] });
    },
  });

  // Update item with optimistic update
  const updateMutation = useMutation({
    mutationFn: async ({ id, updates }: { id: string; updates: Partial<Item> }) => {
      const response = await fetch(`/api/items/${id}`, {
        method: 'PATCH',
        body: JSON.stringify(updates),
      });
      return response.json();
    },
    onMutate: async ({ id, updates }) => {
      await queryClient.cancelQueries({ queryKey: ['items'] });

      // Snapshot current state
      const previousItems = queryClient.getQueryData(['items']);

      // Update store optimistically
      updateItem(id, updates);

      return { previousItems };
    },
    onError: (err, { id }, context) => {
      // Revert on error
      if (context?.previousItems) {
        setItems(context.previousItems);
      }
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ['items'] });
    },
  });

  return {
    items,
    createItem: createMutation.mutate,
    updateItem: updateMutation.mutate,
  };
}
```

### 5. Use in Components

```typescript
// src/components/ItemList.tsx
import { useItems } from '../hooks/useItems';

export function ItemList() {
  const { items, createItem, updateItem } = useItems();

  return (
    <div>
      <button
        onClick={() =>
          createItem({
            title: 'New Item',
            completed: false,
          })
        }
      >
        Add Item
      </button>

      {items?.map((item) => (
        <div key={item.id}>
          <span>{item.title}</span>
          <input
            type="checkbox"
            checked={item.completed}
            onChange={() =>
              updateItem({
                id: item.id,
                updates: { completed: !item.completed },
              })
            }
          />
        </div>
      ))}
    </div>
  );
}
```

## Best Practices

1. **Query Keys**

- Use consistent query key structures
- Include relevant parameters in keys
- Keep keys as specific as needed

2. **Error Handling**

- Always implement rollback logic in onError
- Show user-friendly error messages
- Consider retry strategies

3. **Performance**

- Use appropriate stale times
- Implement proper cache invalidation
- Consider background refetching

4. **State Management**

- Keep server state in React Query
- Use Zustand for UI state
- Separate concerns appropriately

5. **TypeScript**

- Define proper types for all entities
- Use generics with React Query
- Type your Zustand store properly

## Common Patterns

### 1. Optimistic Delete

```typescript
const deleteMutation = useMutation({
  mutationFn: async (id: string) => {
    await fetch(`/api/items/${id}`, { method: 'DELETE' });
  },
  onMutate: async (id) => {
    await queryClient.cancelQueries({ queryKey: ['items'] });
    const previousItems = queryClient.getQueryData(['items']);
    removeItem(id);
    return { previousItems };
  },
  onError: (err, id, context) => {
    if (context?.previousItems) {
      setItems(context.previousItems);
    }
  },
  onSettled: () => {
    queryClient.invalidateQueries({ queryKey: ['items'] });
  },
});
```

### 2. Loading States

```typescript
const { isPending, isError, error } = mutation;

return (
  <div>
    {isPending && <LoadingSpinner />}
    {isError && <ErrorMessage error={error} />}
    {/* ... rest of UI */}
  </div>
);
```

### 3. Batch Updates

```typescript
const batchUpdateMutation = useMutation({
  mutationFn: async (updates: Array<{ id: string; updates: Partial<Item> }>) => {
    const response = await fetch('/api/items/batch', {
      method: 'PATCH',
      body: JSON.stringify(updates),
    });
    return response.json();
  },
  onMutate: async (updates) => {
    await queryClient.cancelQueries({ queryKey: ['items'] });
    const previousItems = queryClient.getQueryData(['items']);

    updates.forEach(({ id, updates }) => {
      updateItem(id, updates);
    });

    return { previousItems };
  },
  onError: (err, updates, context) => {
    if (context?.previousItems) {
      setItems(context.previousItems);
    }
  },
});
```

## Advanced Topics

### 1. Parallel Mutations

Handle multiple optimistic updates simultaneously:

```typescript
const mutations = useMutations(['items']);

// Execute multiple mutations
mutations.mutate([
  { type: 'create', data: newItem1 },
  { type: 'update', data: { id: '1', updates: updates1 } },
  { type: 'delete', data: '2' },
]);
```

### 2. Selective Updates

Update specific parts of the cache:

```typescript
queryClient.setQueryData(['items'], (old: Item[]) =>
  old.map(item =>
    item.id === updatedItem.id
      ? { ...item, ...updatedItem }
      : item
  )
);
```

### 3. Prefetching

Improve perceived performance with prefetching:

```typescript
// Prefetch on hover
const prefetchItem = async (id: string) => {
  await queryClient.prefetchQuery({
    queryKey: ['item', id],
    queryFn: () => fetchItem(id),
  });
};
```

Remember: Optimistic UI is about balancing immediate feedback with data consistency. Always consider the trade-offs between optimistic updates and potential inconsistencies in your specific use case.
