/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
    a = '0b' + a
    b = '0b' + b
    result = BigInt(a) + BigInt(b)
    return result.toString(2)
};