const dateOptions: object = {
  year: "numeric",
  month: "long",
  day: "numeric",
};

const formatDate = (date: Date) =>
  new Date(date).toLocaleDateString("en-US", dateOptions);

export { formatDate };
