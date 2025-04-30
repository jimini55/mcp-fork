# AWS Labs Frontend MCP Server

[![smithery badge](https://smithery.ai/badge/@awslabs/frontend-mcp-server)](https://smithery.ai/server/@awslabs/frontend-mcp-server)

A Model Context Protocol (MCP) server that provides specialized tools for modern web application development.

## Features

### Modern React Application Setup

- Set up a new React frontend application with `BaseUserInterfaceWebApp`
- Includes guidance for configuring React Router, essential dependencies, and Shadcn/UI
- Best practices for project structure and component organization

### Optimistic UI Implementation

- Learn implementation patterns for optimistic UI with `OptimisticUI`
- Leverage React Query and Zustand for efficient state management
- Handle error cases and state rollbacks elegantly

### Authentication Integration

- Integrate authentication with `UsingAmplifyAuthenticator`
- Customize login and signup flows with AWS Amplify
- Manage authenticated state and protected routes

## Prerequisites

1. Install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/) or the [GitHub README](https://github.com/astral-sh/uv#installation)
2. Install Python using `uv python install 3.10`

## Installation

Here are some ways you can work with MCP across AWS, and we'll be adding support to more products including Amazon Q Developer CLI soon: (e.g. for Amazon Q Developer CLI MCP, `~/.aws/amazonq/mcp.json`):

```json
{
  "mcpServers": {
    "awslabs.frontend-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.frontend-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## Usage

The Frontend MCP Server provides three primary tools for modern web application development:

### BaseUserInterfaceWebApp

Learn about how to start up a new UI frontend web app with modern best practices.

This tool provides guidance on:

- Scaffolding a new React Router application
- Installing essential dependencies (Zustand, Zod, AWS Amplify, React Query)
- Setting up Shadcn/UI components
- Configuring the project structure

### OptimisticUI

Learn how to implement optimistic UI patterns with React Query and Zustand.

This tool covers:

- Core concepts of optimistic UI
- Step-by-step implementation with React Query and Zustand
- Code examples for common patterns
- Best practices for error handling and state management
- Advanced topics like parallel mutations and prefetching

### UsingAmplifyAuthenticator

Learn how to use the Amplify Authenticator for authentication in React applications.

This tool provides:

- Complete examples for setting up Amplify Authenticator
- Guidance on customizing the authentication UI
- Patterns for handling authentication state
- Integration with React Router for protected routes
- Strategies for managing user attributes and sessions
