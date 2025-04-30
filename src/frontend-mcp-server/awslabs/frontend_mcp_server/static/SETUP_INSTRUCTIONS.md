# Setting up a new React frontend web app

## Scaffold a new React Router app

```bash
npx create-react-router@latest . --template=remix-run/react-router-templates/default --yes
npm install
```

Add some frequently used dependencies:

```bash
npm install zustand zod aws-amplify @aws-amplify/backend-cli @aws-amplify/ui-react @tanstack/react-query
npm install -D @biomejs/biome @tanstack/react-query-devtools
npx @biomejs/biome init
```

## Set up Shadcn/UI

1. Add resolve alias to your `vite.config.js`:

```javascript
import { reactRouter } from "@react-router/dev/vite";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineConfig({
  plugins: [tailwindcss(), reactRouter(), tsconfigPaths()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
});
```

2. Run the following command to install Shadcn/UI:

```bash
npx shadcn@canary init --defaults --force --yes
```

3. Run the following command to install the UI components:

```bash
npx shadcn@canary add button --yes
```

Or install all components at once:

```bash
npx shadcn@canary add --all --yes
```
