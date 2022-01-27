db.createUser(
    {
        user: 'root',
        pwd: 'mongo',
        roles: [
            {
                role: 'dbOwner',
                db: 'iot',
            },
        ],
    }
);
  
db.auth('root', 'mongo')
  
db = db.getSiblingDB('iot');
  
db.createCollection( 
    "Admins", 
    {
        validator:{
            $jsonSchema:{
                bsonType:"object",
                properties:{
                    login:{
                        bsonType:"string",
                        description:"must be a string and is required"
                    },
                    password:{
                        bsonType:"string",
                        description:"must be a string and is required"
                    }
                }
            }
        }
    }
);

db.createCollection( 
    "Users",
    {
        validator:{
            $jsonSchema:{
                bsonType:"object",
                properties:{
                    surname:{
                        bsonType:"string",
                        description:"must be a string and is required"
                    },
                    name:{
                        bsonType:"string",
                        description:"must be a string and is required"
                    },
                    email:{
                        bsonType:"string",
                        description:"must be a string and is required"
                    },
                    status:{
                        enum:[
                            "ACTIVE",
                            "DISABLED"
                        ],
                        
                    },
                    current_visit:{
                        bsonType:"object",
                        properties:{
                            visit_start:{
                                bsonType:"string",
                                description:"must be a date and is required"
                            },
                            cost_per_min:{
                                bsonType:"int",
                                description:"must be an int"
                            },
                            visit_type:{
                                bsonType:"objectId",
                                description:"must be an int"
                            }
                        }
                    },
                    card:{
                        bsonType:"string",
                        description:"must be a string"
                    },
                }
            }
        }
    }
)
  
db.createCollection( 
    "VisitTypes",
    {
        validator:{
            $jsonSchema:{
                bsonType:"object",
                properties:{
                    visit_type:{
                        bsonType:"string",
                        description:"must be a string and is required"
                    },
                    cost_per_min:{
                        bsonType:"int",
                        description:"cost in groszy"
                    },
                    rfid_scanner:{
                        bsonType:"string",
                        description:"the id of the rfid scanner at the gate"
                    },
                    
                }
            }
        }
    }
);
