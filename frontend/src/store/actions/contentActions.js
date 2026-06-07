export const SET_CONTENT = 'SET_CONTENT';
export const ADD_CONTENT = 'ADD_CONTENT';
export const REMOVE_CONTENT = 'REMOVE_CONTENT';

export const setContent = (content) => ({ type: SET_CONTENT, payload: content });
export const addContent = (content) => ({ type: ADD_CONTENT, payload: content });
export const removeContent = (id) => ({ type: REMOVE_CONTENT, payload: id });
