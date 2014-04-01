/* 

How many days has passed since the start of the year?

Get days difference

This was an interview question

 */

/*

params: date in the formart "month.day.year"
ex: 02.01.2013

*/

var chai = require("chai");

function getDay(date){
  var inputDate = date.split(".");
  var inputYear = inputDate[2];
  var inputDay = inputDate[1];
  var inputMonth = inputDate[0];

  var oneDay = 24*60*60*1000;
  var firstDate = new Date(inputYear-1+","+"12"+","+"31");
  var secondDate = new Date(inputYear+","+inputMonth+","+inputDay);

  var diffDays = Math.round(Math.abs((secondDate.getTime() - firstDate.getTime())/(oneDay)));

  return diffDays;
}

var expect = chai.expect;

expect(getDay("03.01.2013")).to.equal(60); //regular year test
expect(getDay("03.01.2012")).to.equal(61); //leap year test