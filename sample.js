myObj={    "people" : [
      {
         "firstName": "Joe",
         "lastName": "Jackson",
         "gender": "male",
         "age": 28,
         "number": "7349282382",
         "active" : true
      },
      {
         "firstName": "James",
         "lastName": "Smith",
         "name": ["James","Smith"],
         "gender": "male",
         "age": 32,
         "number": "5678568567",
         "active" : false
      },
      {
         "firstName": "Emily",
         "lastName": "Jones",
         "gender": "female",
         "age": 24,
         "number": "456754675",
         "active" : true
      }
    ]
  }

console.log(myObj.people[1].lastName)
console.log(myObj.people[1].firstName)

console.log(typeof myObj.people[1].age)
console.log(typeof myObj.people[1].firstName)
console.log(typeof myObj.people[1].active)


console.log(myObj.people[0])
console.log(myObj.people[1].name[0])
console.log(myObj.people[1].name[1])