db.createUser({
  user: 'root',
  pwd: 'mongo',
  roles: [
    {
      role: 'readWrite',
      db: 'rental',
    },
  ],
});
db.auth('root', 'mongo')

db = db.getSiblingDB('iotDB');

db.createCollection( "Users", {
    validator: { $jsonSchema: {
        bsonType: "object",
        properties: {
            surname: {
                bsonType : "string",
                description: "must be a string and is required"
            },
            name: {
                bsonType : "string",
                description: "must be a string and is required"
            },
            balance: {
                bsonType : "int",
                description: "balance in groszy"
            },
            email: {
                bsonType : "string",
                description: "must be a string and is required"
            },
            status:{
                enum: ["ACTIVE","DISABLED"],
            },
            currentVisit: {
                bsonType: "object",
                properties: {
                    visitStart: {
                        bsonType: "string",
                        description: "must be a date and is required"
                    },
                    costPerMin: {
                        bsonType: "string",
                        description: "must be a string"
                    },
                    visitType: {
                        bsonType: "int",
                        description: "must be an int"
                    }
                }
            },
            cards: {
                bsonType: "array",
                items: {
                    bsonType: "string",
                    description: "must be a string and is required"
                }
            },
        }
    } }
} );

db.createCollection( "VisitTypes", {
    validator: { $jsonSchema: {
        bsonType: "object",
        properties: {
            visitType: {
                bsonType: "string",
                description: "must be a string and is required"
            },
            costPerMin: {
                bsonType: "int",
                description: "cost in groszy"
            },
            RFIDScanner: {
                bsonType: "string",
                description: "the id of the rfid scanner at the gate"
            },
        }
    } }
} );

db.createCollection( "VisitArchive", {
    validator: { $jsonSchema: {
        bsonType: "object",
        properties: {
            visitStart: {
                bsonType: "string",
                description: "must be a date and is required"
            },
            visitEnd:{
                bsonType: "string",
                description: "must be a date and is required"
            },
            costPerMin: {
                bsonType: "int",
                description: "cost in groszy"
            },
            totalCost: {
                bsonType: "int",
                description: "cost in groszy"
            },
            visitType: {
                bsonType: "int",
                description: "must be an int"
            },
            user:{
                bsonType: "int",
                description: "must be an int"
            }
        }   
    } }   
} 
);