let input = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
input = BigInt(input.toString().replace(/,/g, '')) + 1n
answer = []
for (item of String(input)){
    answer.push(Number(item))
}

console.log(answer)
