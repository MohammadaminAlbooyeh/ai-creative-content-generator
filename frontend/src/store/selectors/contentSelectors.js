export const selectAllContent = (state) => state.content.items;

export const selectContentById = (state, id) =>
  state.content.items.find((c) => c.id === id);

export const selectContentByType = (state, contentType) =>
  state.content.items.filter((c) => c.content_type === contentType);
