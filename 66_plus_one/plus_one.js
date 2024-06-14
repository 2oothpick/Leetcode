let input = [1,2,3]
input = Number(input.toString().replace(/,/g, '')) + 1
answer = []
for (item of String(input)){
    answer.push(Number(item))
}

console.log(answer)
