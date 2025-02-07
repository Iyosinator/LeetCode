/**
 * @param {number} celsius
 * @return {number[]}
 */
var convertTemperature = function(celsius) {
    k = celsius + 273.15
    f = celsius*1.80 + 32
    return [k,f]
};