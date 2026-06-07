export const START_GENERATION = 'START_GENERATION';
export const GENERATION_SUCCESS = 'GENERATION_SUCCESS';
export const GENERATION_FAILURE = 'GENERATION_FAILURE';
export const CLEAR_RESULT = 'CLEAR_RESULT';

export const startGeneration = () => ({ type: START_GENERATION });
export const generationSuccess = (result) => ({ type: GENERATION_SUCCESS, payload: result });
export const generationFailure = (error) => ({ type: GENERATION_FAILURE, payload: error });
export const clearResult = () => ({ type: CLEAR_RESULT });
