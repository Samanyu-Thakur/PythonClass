num = [1,2,3,4,5]
let = ['a', 'b','c','d'] # type: ignore
print(num)
print(let)


mix = let + num
let += num
print(mix)
print(let)
print(let[2])
print(let[4],[1])