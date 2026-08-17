console.log("===세 번째 js===")

const isMember = true
const hasCoupon = true
const isSuspended = true

if ((isMember || hasCoupon) && !isSuspended) {
    console.log("수강 가능")
} else {
    console.log("수강 불가")
}