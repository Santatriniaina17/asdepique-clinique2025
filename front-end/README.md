Libs uses:
- Material UI – UI components library
- TanStack React Query – Data fetching and caching
- xlsx & file-saver – Export to Excel files
- i18next – Language translation support
- Redux – Global app state management
- jsPDF – Create PDF documents
- moment.js – Work with dates and times
- notistack – Show notifications (snackbars)
- react-hook-form – Manage forms easily
- Swiper – Carousel/slider UI
- Storybook – Develop and document UI components separately
- MSW (Mock Service Worker) – Mock APIs during development and tests
- jose – Token creation (Only used in auth mock)

API flow: component → hook → service → api (eventually: → mock)
Component flow: App → page → feature → (layout) → shared

Code architecture:

App.tsx                         # Root component of the application
main.tsx                        # Application entry point
src/
├── app/
│   ├── config.ts               # Global app configuration (URLs, options, etc.)
│   └── routes/               
│       ├── ProtectedRoute/     # Wrapper for pages with conditionnal access
│       ├── paths.ts            # App paths list
│       └── router.ts           # Main route definitions and setup
│
├── pages/                      # General/global pages (e.g., NotFound, Login, Home)
│   └── {page_name}/
│       ├── {page_name}.tsx
│       ├── {page_name}.types.ts
│       ├── {page_name}.styles.ts
│       └── route.tsx           # Page-specific route declaration
│
├── features/                   # Modular business features
│   └── {feature_name}/
│       ├── api/                # Feature-specific API calls
│       ├── components/         # Components related to the feature
│       ├── hooks/              # Custom hooks used within the feature
│       ├── providers/          
│       ├── services/           # Business logic and services
│       ├── slices/             # Redux slices
│       └── types.ts            # TypeScript types used within the feature
│
├── shared/                     # Reusable elements shared across the app
│   ├── components/             # Reusable UI components (buttons, inputs, etc.)
│   ├── hooks/                  # Shared custom hooks
│   ├── utils/                  # General-purpose utility functions
│   ├── themes/                 # Application theme configuration
│   └── constants/              # Global constants
│
├── mocks/                      # API mocks for development and testing
│
└── i18n/                       # Translations
    ├── index.ts                # i18n initialization and configuration
    └── locales/                # Language-specific translation dictionaries
        └── {language_name}/
            └── translation.json