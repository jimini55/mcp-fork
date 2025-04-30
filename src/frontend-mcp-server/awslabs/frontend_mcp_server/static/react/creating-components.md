# Creating Components with shadcn/ui and AWS Amplify

When creating new components for your AWS-powered application, always check if there is a shadcn component that can be used instead of creating custom components.

This will improve the maintainability of the application and simplify the codebase.

## Installing shadcn Components

Install shadcn/ui components as needed. You must use the --force flag to avoid dependency issues:

```bash
npx shadcn@latest add button
```

## AWS Amplify UI Components

For authentication and other AWS-specific functionality, use the pre-built Amplify UI components:

```bash
npm install @aws-amplify/ui-react
```

Example usage with shadcn components:

```tsx
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Authenticator } from '@aws-amplify/ui-react';

export function LoginCard() {
  return (
    <Card className="w-[400px]">
      <CardHeader>
        <CardTitle>Sign In</CardTitle>
      </CardHeader>
      <CardContent>
        <Authenticator />
      </CardContent>
    </Card>
  );
}
```

## Best Practice

When building AWS-powered applications, prefer using the official Amplify UI components for AWS-specific functionality and shadcn components for general UI elements.
