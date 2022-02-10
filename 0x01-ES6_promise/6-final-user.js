import signUpUser from './4-user-promise'
import uploadPhoto from './5-photo-reject'

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.resolve(Promise.all([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((val) => {
      console.log(val);
      return { status: 'fulfilled', value: val }
    })
    .catch((val) => {
      return { status: 'reject', value: val }
    })
  )
}
