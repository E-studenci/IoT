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
  
db.createCollection( 
    "VisitArchive",
    {
        validator:{
            $jsonSchema:{
                bsonType:"object",
                properties:{
                    visit_start:{
                        bsonType:"string",
                        description:"must be a date and is required"
                    },
                    visit_end:{
                        bsonType:"string",
                        description:"must be a date and is required"
                    },
                    cost_per_min:{
                        bsonType:"int",
                        description:"cost in groszy"
                    },
                    total_cost:{
                        bsonType:"int",
                        description:"cost in groszy"
                    },
                    visit_type:{
                        bsonType:"objectId",
                        description:"must be an int"
                    },
                    user:{
                        bsonType:"objectId",
                        description:"must be an int"
                    }
                }
            }
        }
    }
);
db.Admins.insertMany([
    {
		login: "admin1",
		password: "password1"
    },
	{
		login: "admin2",
		password: "password2"
    }
])

db.Users.insertMany([
    {
		surname: "Snow",
		name: "Zidan",
		email: "example1@gmail.com",
		status: "ACTIVE",
		card: "f91a61e515d1fc6a7fa9986473b6d0ff"
    },
	{
		surname: "Sean",
		name: "Buckley",
		email: "example2@gmail.com",
		status: "ACTIVE",
		card: "9827bce49e2b5b9ea09f69db59c20e85"
    },
    {
		surname: "Jolene",
		name: "Alvarado",
		email: "example3@gmail.com",
		status: "ACTIVE",
		card: "85bc3f25732df73426aa44f59c6ec78c"
    },
    {
		surname: "Maxim",
		name: "Witt",
		email: "example4@gmail.com",
		status: "ACTIVE",
		card: "bdef2adeeede3e4502c6d891b0a0e3e4"
    },
    {
		surname: "Tylor",
		name: "Santiago",
		email: "example5@gmail.com",
		status: "DISABLED",
		card: "44963461cf009e75c11447da27aec4ed"
    }
])

db.VisitTypes.insertMany([
    {
        visit_type: "Gym",
        cost_per_min: 60,
        rfid_scanner: "f91a61e515d1fc6a7fa9986473b6d0ff"
    },
    {
        visit_type: "Pool",
        cost_per_min: 70,
        rfid_scanner: "9827bce49e2b5b9ea09f69db59c20e85"
    },
    {
        visit_type: "Spa",
        cost_per_min: 50,
        rfid_scanner: "85bc3f25732df73426aa44f59c6ec78c"
    },
    {
        visit_type: "Sauna",
        cost_per_min: 100,
        rfid_scanner: "bdef2adeeede3e4502c6d891b0a0e3e4"
    }
])