/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
    const result = parseInt(a, 2) + parseInt(b, 2)
    return (result >>> 0).toString(2)
};