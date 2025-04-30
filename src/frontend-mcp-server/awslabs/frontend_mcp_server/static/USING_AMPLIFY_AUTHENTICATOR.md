# Using Amplify Authenticator

Login.tsx EXAMPLE

```typescript
import { Authenticator, useAuthenticator } from "@aws-amplify/ui-react"
import { useEffect } from "react"
import { useLocation, useNavigate } from "react-router-dom"
import "@aws-amplify/ui-react/styles.css"
import "@/styles/login.css"
import { useUserStore } from "@/stores/user-store"
import { type SignInInput, fetchUserAttributes, signIn, signOut } from "aws-amplify/auth"
import { I18n } from "aws-amplify/utils"

I18n.putVocabulariesForLanguage("en", {
	"Sign In": "Login", // Tab header
	"Sign in": "Login", // Button label
	"Sign in to your account": "Welcome back!",
	Username: "Enter your username", // Username label
	Password: "Enter your password", // Password label
	"Forgot your password?": "Reset password",
	"Create Account": "Register", // Tab header
})

const components = {
	Header: () => (
		<h1 className="flex items-center justify-center p-4 font-bold text-2xl">My Web App</h1>
	),
	SignIn: {
		Header: () => (
			<h1 className="flex items-center justify-center p-4 font-bold text-2xl">Welcome back 👋</h1>
		),
	},
	SignUp: {
		Header: () => (
			<h1 className="flex items-center justify-center p-4 font-bold text-2xl">
				Create your account 🚀
			</h1>
		),
	},
	Footer: () => (
		<p className="flex items-center justify-center p-4 font-mono text-sm">© 2024 My Web App</p>
	),
}
const formFields = {
	signIn: {
		username: {
			placeholder: "Enter your email:",
		},
		password: {
			placeholder: "Enter your password:",
		},
	},
	signUp: {
		password: {
			label: "Password",
			placeholder: "Enter your password:",
			order: 1,
		},
		confirm_password: {
			label: "Confirm password",
			placeholder: "Confirm your password:",
			order: 2,
		},
		email: {
			placeholder: "Enter your email:",
			order: 3,
		},
		given_name: {
			label: "First name",
			placeholder: "Enter your first name:",
			order: 4,
		},
		family_name: {
			label: "Last name",
			placeholder: "Enter your last name:",
			order: 5,
		},
	},
	forceNewPassword: {
		password: {
			placeholder: "Enter your password:",
		},
	},
	forgotPassword: {
		username: {
			placeholder: "Enter your email:",
		},
	},
}

const Login: React.FC = () => {
	const { authStatus } = useAuthenticator((context) => [context.authStatus])
	const setUserAttributes = useUserStore((state) => state.setUserAttributes)

	const navigate = useNavigate()
	const location = useLocation()

	// Improved navigation after authentication
	useEffect(() => {
		if (authStatus === "authenticated") {
			// More robust navigation state handling
			const defaultPath = "/{SOME WEB PAGE YOU WANT TO GO TO AFTER LOGIN}"
			let navigateTo = defaultPath

			// Type-safe state access with proper fallbacks
			if (
				location.state &&
				typeof location.state === "object" &&
				"from" in location.state &&
				location.state.from &&
				typeof location.state.from === "object" &&
				"pathname" in location.state.from &&
				typeof location.state.from.pathname === "string"
			) {
				navigateTo = location.state.from.pathname
			}

			// Preserve query parameters if they exist
			const searchParams = new URLSearchParams(location.search)
			const queryString = searchParams.toString()
			const fullPath = queryString ? `${navigateTo}?${queryString}` : navigateTo

			// Navigate with state to indicate this was a post-auth redirect
			navigate(fullPath, {
				replace: true,
				state: { postAuthRedirect: true },
			})
		}
	}, [authStatus, navigate, location])

	const services = {
		handleSignIn: async (input: SignInInput) => {
			const signInResult = await signIn(input)
			if (signInResult) {
				fetchUserAttributes().then(setUserAttributes)
			}
			return signInResult
		},
		handleSignOut: async () => {
			await signOut()
			setUserAttributes(null)
		},
	}
	return (
		<div className="flex items-center justify-center">
			{/* <ThemeProvider theme={theme} colorMode={themeMode as ColorMode}>
				<Authenticator formFields={formFields} components={components} services={services} />
			</ThemeProvider> */}
			<Authenticator formFields={formFields} components={components} services={services} />
		</div>
	)
}
export default Login
```

App.tsx example

```typescript
import Header from "@/components/layout/Header"
import { AppSidebar } from "@/components/layout/Sidebar/AppSidebar"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
import { ThemeProvider } from "@/hooks/theme-provider"
import { AppRoutes } from "@/routes/"
import { Authenticator } from "@aws-amplify/ui-react"
import { QueryClient, QueryClientProvider } from "@tanstack/react-query"
import { ReactQueryDevtools } from "@tanstack/react-query-devtools"
import { Amplify } from "aws-amplify"
import type React from "react"
import { BrowserRouter as Router } from "react-router-dom"
import config from "../amplify_outputs.json"

Amplify.configure({
	auth: config.auth,
	data: {
		...config.data,
		authorization_types: [config.data.default_authorization_type],
	},
	version: config.version,
})

const queryClient = new QueryClient()

const App: React.FC = () => {
	return (
		<ThemeProvider>
			<Authenticator.Provider>
				<QueryClientProvider client={queryClient}>
					<Router future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
						<SidebarProvider defaultOpen={false}>
							<AppSidebar variant="inset" collapsible="icon" />
							<SidebarInset>
								<Header />
								<AppRoutes />
							</SidebarInset>
						</SidebarProvider>
					</Router>
					<ReactQueryDevtools />
				</QueryClientProvider>
			</Authenticator.Provider>
		</ThemeProvider>
	)
}

export default App
```