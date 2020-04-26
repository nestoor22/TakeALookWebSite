export const getPreparedBoardDataForCreation = (data) => {
  return {
    name: data.name,
    backgroundColor: data.color,
    isOpen: data.type === "Public",
    isPrivate: data.type === "Private",
  };
};
