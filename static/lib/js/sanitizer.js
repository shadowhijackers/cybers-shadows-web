var SURROGATE_PAIR_REGEXP = /[\uD800-\uDBFF][\uDC00-\uDFFF]/g;
  // Match everything outside of normal chars and " (quote character)
var NON_ALPHANUMERIC_REGEXP = /([^\#-~| |!])/g;

var Sanitizer = (function(){

   function Sanitizer(){
        console.log("SANITIZER MODULE LOADED")
   }

   /**
    * Escapes all potentially dangerous characters, so that the
    * resulting string can be safely inserted into attribute or
    * element text.
    * @param value
    * @returns {string} escaped text
    * @link https://github.com/angular/angular.js/blob/v1.3.14/src/ngSanitize/sanitize.js#L435
    */
   Sanitizer.encodeEntities = function(value) {
     return value.
        replace(/&/g, '&amp;').
        replace(SURROGATE_PAIR_REGEXP, function(value) {
        var hi = value.charCodeAt(0);
        var low = value.charCodeAt(1);
        return '&#' + (((hi - 0xD800) * 0x400) + (low - 0xDC00) + 0x10000) + ';';
        }).
        replace(NON_ALPHANUMERIC_REGEXP, function(value) {
        return '&#' + value.charCodeAt(0) + ';';
        }).
        replace(/</g, '&lt;').
        replace(/>/g, '&gt;');
    }

 return Sanitizer

}())

