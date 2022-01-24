<template>
    <div>
        <NavBarAdmin />
        <div class="row container-fluid h-100">
        <div class="col-sm-4 offset-md-1">
            <h4>Klienci na siłowni</h4>
            <ol class="list-group list-group-numbered" v-for="client in ongoingClients" :key="client._id">
                <li class="list-group-item d-flex justify-content-between align-items-start list-group-item-secondary">
                  <div class="ms-2 me-auto">
                    <div class="fw-bold">{{ client.surname }} {{ client.name }}</div>
                    Godzina wejścia: {{ client.current_visit.visit_start }}
                  </div>
                </li>
            </ol>
        </div>
        <div class="col-sm-6">
            <h4>Klienci w kolejce do zapłaty</h4>
            <ul class="list-group" v-for="client in pendingClients" :key="client._id">
                <li class="list-group-item d-flex justify-content-between align-items-start list-group-item-secondary">
                    <div class="ms-2 me-auto">
                      <h5 class="mb-1">{{ client.user.surname }} {{ client.user.name }}</h5>
                      <small>Czas: {{ (Date.parse(client.visit_end) - Date.parse(client.visit_start))/1000 }}min</small><br />
                      <small>Do zapłaty: {{ client.cost_per_min * (Date.parse(client.visit_end) - Date.parse(client.visit_start))/100000 }} zł</small>
                    </div>
                    <b-button class="btn btn-dark float-right" @click="deletePendingClient(client._id)" id="submitPaymentBtn" type="button">Zatwierdź</b-button> 
                </li>
            </ul>
        </div>
    </div>
    </div>
</template>

<script>
import NavBarAdmin from '../components/NavBarAdmin.vue'
import axios from 'axios'

export default {
    components: { NavBarAdmin },
    name: "CurrentClients",
    methods: {
        deletePendingClient(id) {
            console.log(id)
        }
    },
    data() {
      return {
        pendingClients: [{
            "_id": "61e7516be2ed2b9d91a8687b",
            "visit_start": "2022/01/18 23:46:51",
            "visit_end": "2022/01/18 23:47:22",
            "cost_per_min": 70,
            "total_cost": 36,
            "visit_type": {
                "_id": "61e750ddecd8897aa62de65b",
                "visit_type": "Pool",
                "cost_per_min": 70,
                "rfid_scanner": "9827bce49e2b5b9ea09f69db59c20e85"
            },
            "user": {
                "_id": "61e750e6ecd8897aa62de665",
                "surname": "Tylor",
                "name": "Santiago",
                "balance": 5000,
                "email": "example5@gmail.com",
                "status": "DISABLED",
                "card": "44963461cf009e75c11447da27aec4ed"
            },
            "status": "PENDING"
        },
        {
            "_id": "61e75180e2ed2b9d91a8687c",
            "visit_start": "2022/01/18 23:47:12",
            "visit_end": "2022/01/18 23:48:42",
            "cost_per_min": 70,
            "total_cost": 105,
            "visit_type": {
                "_id": "61e750ddecd8897aa62de65b",
                "visit_type": "Pool",
                "cost_per_min": 70,
                "rfid_scanner": "9827bce49e2b5b9ea09f69db59c20e85"
            },
            "user": {
                "_id": "61e750e6ecd8897aa62de663",
                "surname": "Jolene",
                "name": "Alvarado",
                "balance": 1000,
                "email": "example3@gmail.com",
                "status": "ACTIVE",
                "card": "85bc3f25732df73426aa44f59c6ec78c"
            },
            "status": "PENDING"
        },
        {
            "_id": "61e75194e2ed2b9d91a8687d",
            "visit_start": "2022/01/18 23:47:32",
            "visit_end": "2022/01/18 23:48:52",
            "cost_per_min": 70,
            "total_cost": 94,
            "visit_type": {
                "_id": "61e750ddecd8897aa62de65b",
                "visit_type": "Pool",
                "cost_per_min": 70,
                "rfid_scanner": "9827bce49e2b5b9ea09f69db59c20e85"
            },
            "user": {
                "_id": "61e750e6ecd8897aa62de664",
                "surname": "Maxim",
                "name": "Witt",
                "balance": 2000,
                "email": "example4@gmail.com",
                "status": "ACTIVE",
                "card": "bdef2adeeede3e4502c6d891b0a0e3e4"
            },
            "status": "PENDING"
        }],
        ongoingClients: [{
            "_id": "61e750e6ecd8897aa62de661",
            "surname": "Snow",
            "name": "Zidan",
            "balance": 3000,
            "email": "example1@gmail.com",
            "status": "ACTIVE",
            "card": "f91a61e515d1fc6a7fa9986473b6d0ff",
            "current_visit": {
                "_id": "61e751c6e2ed2b9d91a86880",
                "visit_start": "2022/01/18 23:48:22",
                "cost_per_min": 70,
                "visit_type": {
                    "_id": "61e750ddecd8897aa62de65b",
                    "visit_type": "Pool",
                    "cost_per_min": 70,
                    "rfid_scanner": "9827bce49e2b5b9ea09f69db59c20e85"
                }
            }
        },
        {
            "_id": "61e750e6ecd8897aa62de662",
            "surname": "Sean",
            "name": "Buckley",
            "balance": 7000,
            "email": "example2@gmail.com",
            "status": "ACTIVE",
            "card": "9827bce49e2b5b9ea09f69db59c20e85",
            "current_visit": {
                "_id": "61e7519ee2ed2b9d91a8687e",
                "visit_start": "2022/01/18 23:47:42",
                "cost_per_min": 70,
                "visit_type": {
                    "_id": "61e750ddecd8897aa62de65b",
                    "visit_type": "Pool",
                    "cost_per_min": 70,
                    "rfid_scanner": "9827bce49e2b5b9ea09f69db59c20e85"
                }
            }
        },
        {
            "_id": "61e750e6ecd8897aa62de664",
            "surname": "Maxim",
            "name": "Witt",
            "balance": 2000,
            "email": "example4@gmail.com",
            "status": "ACTIVE",
            "card": "bdef2adeeede3e4502c6d891b0a0e3e4",
            "current_visit": {
                "_id": "61e751eee2ed2b9d91a86881",
                "visit_start": "2022/01/18 23:49:02",
                "cost_per_min": 70,
                "visit_type": {
                    "_id": "61e750ddecd8897aa62de65b",
                    "visit_type": "Pool",
                    "cost_per_min": 70,
                    "rfid_scanner": "9827bce49e2b5b9ea09f69db59c20e85"
                }
            }
        },
        {
            "_id": "61e750e6ecd8897aa62de665",
            "surname": "Tylor",
            "name": "Santiago",
            "balance": 5000,
            "email": "example5@gmail.com",
            "status": "DISABLED",
            "card": "44963461cf009e75c11447da27aec4ed",
            "current_visit": {
                "_id": "61e751bce2ed2b9d91a8687f",
                "visit_start": "2022/01/18 23:48:12",
                "cost_per_min": 70,
                "visit_type": {
                    "_id": "61e750ddecd8897aa62de65b",
                    "visit_type": "Pool",
                    "cost_per_min": 70,
                    "rfid_scanner": "9827bce49e2b5b9ea09f69db59c20e85"
                }
            }
        }
    ]}},
    async created() {
        // const response = await axios.get('user', {
        //     headers: {
        //         Authorization: 'Bearer' + localStorage.getItem('token')
        //     }
        // })

        // console.log(response)
    },
    // mounted() {
    //   fetch('http://130.61.111.97:20001/visit/get_ongoing')
    //   .then((res) => res.json())
    //   .then(data => this.clients = data)
    //   .catch(err => console.log(err.message))
    //   console.log(this.clients)
    // }
}
</script>

<style>
h4 {
    margin-top: 10px;
}
</style>