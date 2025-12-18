import { combineReducers } from '@reduxjs/toolkit';
import themeReducer from '../../features/theme/slices/theme.slice'

const rootReducer = combineReducers({
    theme: themeReducer,
})

export default rootReducer