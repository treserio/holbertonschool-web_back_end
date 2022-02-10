import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  return [
    await signUpUser(firstName, lastName)
      .then((val) => ({ status: 'fulfilled', value: val })),
    await uploadPhoto(fileName)
      .catch((val) => ({ status: 'rejected', value: val.toString() })),
  ];
}
