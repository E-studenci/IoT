<template>
    <div>
        <NavBarAdmin />
        <div class="row container-fluid h-100">
        <div class="col-sm-4 offset-md-1">
            <h4>Obecni Klienci</h4>
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
                      <small>Czas: {{ (Date.parse(client.visit_end) - Date.parse(client.visit_start))/1000 }}min  |  </small>
                      <small>Do zapłaty: {{ client.cost_per_min * (Date.parse(client.visit_end) - Date.parse(client.visit_start))/100000 }} zł</small><br />
                      <small>Sektor: {{ client.visit_type.visit_type }}</small>
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
        findPendingClients() {
            var myHeaders = new Headers();
            myHeaders.append("Cookie", document.cookie);
            
            var requestOptions = {
                method: 'GET',
                headers: myHeaders,
                credentials: 'include',
            };

            fetch(process.env.API_URL + "visit/get_pending", requestOptions)
            .then((res) => {
                if(res.ok) {
                    return res.json()
                }
                else if(res.status == '401') {
                    this.$router.push('/login')
                }
            })
            .then(data => {
                this.pendingClients = data.data
            })
        },
        findOngoingClients() {
            var myHeaders = new Headers();
            myHeaders.append("Cookie", document.cookie);
            var requestOptions = {
                method: 'GET',
                headers: myHeaders,
                credentials: 'include',
            };

            fetch(process.env.API_URL + "visit/get_ongoing", requestOptions)
            .then((res) => {
                if(res.ok) {
                    return res.json()
                }
                else if(res.status == '401') {
                    this.$router.push('/login')
                }
            })
            .then(data => {
                this.ongoingClients = data.data
            })
        },
        deletePendingClient(id) {
            var myHeaders = new Headers();
            myHeaders.append("Cookie", document.cookie);
            var url = process.env.API_URL + "visit/confirm/" + id

            var requestOptions = {
                method: 'POST',
                headers: myHeaders,
                credentials: 'include',
            };

            fetch(url, requestOptions)
            .then(this.findPendingClients())
        }
    },
    data() {
      return {
        pendingClients: [],
        ongoingClients: []
      }
    },
    created() {
        
    },
    mounted() {
      this.findPendingClients()
      this.findOngoingClients()
    }
}
</script>

<style>
h4 {
    margin-top: 10px;
}
</style>