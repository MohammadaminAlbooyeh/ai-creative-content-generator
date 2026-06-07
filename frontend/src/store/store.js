import { createStore, combineReducers, applyMiddleware } from 'redux';
import { thunk } from 'redux-thunk';
import contentReducer from './reducers/contentReducer';
import generationReducer from './reducers/generationReducer';
import userReducer from './reducers/userReducer';

const rootReducer = combineReducers({
  content: contentReducer,
  generation: generationReducer,
  user: userReducer,
});

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;
