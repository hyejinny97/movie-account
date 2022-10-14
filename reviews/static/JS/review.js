const grade = document.querySelector('#grade')
const review_stars = document.querySelectorAll('.review-star')

console.log(grade)
console.log(grade.value)
console.log(review_stars)
console.log(review_stars[0])

for (let review_star of review_stars) {
  if (review_star.value == grade.value) {
    review_star.setAttribute('checked', 'True')
  }
}