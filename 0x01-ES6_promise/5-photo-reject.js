import signUpUser from "./4-user-promise";

export default function uploadPhoto(filename) {
  return Promise.reject(Error(`${filename} cannot be processed`));
}
