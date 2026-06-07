import { START_GENERATION, GENERATION_SUCCESS, GENERATION_FAILURE, CLEAR_RESULT } from '../actions/generationActions';

const initialState = { loading: false, result: null, error: null };

export default function generationReducer(state = initialState, action) {
  switch (action.type) {
    case START_GENERATION:
      return { ...state, loading: true, error: null };
    case GENERATION_SUCCESS:
      return { loading: false, result: action.payload, error: null };
    case GENERATION_FAILURE:
      return { loading: false, result: null, error: action.payload };
    case CLEAR_RESULT:
      return { ...state, result: null };
    default:
      return state;
  }
}
