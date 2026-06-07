import { SET_CONTENT, ADD_CONTENT, REMOVE_CONTENT } from '../actions/contentActions';

const initialState = { items: [] };

export default function contentReducer(state = initialState, action) {
  switch (action.type) {
    case SET_CONTENT:
      return { ...state, items: action.payload };
    case ADD_CONTENT:
      return { ...state, items: [...state.items, action.payload] };
    case REMOVE_CONTENT:
      return { ...state, items: state.items.filter((c) => c.id !== action.payload) };
    default:
      return state;
  }
}
