import { SET_USER, LOGOUT } from '../actions/userActions';

const initialState = { currentUser: null };

export default function userReducer(state = initialState, action) {
  switch (action.type) {
    case SET_USER:
      return { ...state, currentUser: action.payload };
    case LOGOUT:
      return { ...state, currentUser: null };
    default:
      return state;
  }
}
