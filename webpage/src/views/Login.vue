<template>
    <div>
        <NavBar />
        <h2>Siłownia fitness - klub z zasadami</h2>
            <section class="photos">
                <div class="container-fluid h-100 row">
                    <div class="col-sm-5 offset-md-1">

                        <div class="row">
                            <div class="col-sm-6">
                            <figure>
                                <b-img :src="require('../../static/images/sala.jpg')"/>
                            </figure>
                            </div>
                            <div class="col-sm-6">
                            <figure>
                                <b-img :src="require('../../static/images/hantle.jpg')"/>
                            </figure>
                            </div>
                            <div class="col-sm-6">
                            <figure>
                                <b-img :src="require('../../static/images/bieznie.jpg')"/>
                            </figure>
                            </div>
                            <div class="col-sm-6">
                            <figure>
                                <b-img :src="require('../../static/images/lawa.jpg')"/>
                            </figure>
                            </div>
                            <div class="col-sm-6">
                            <figure>
                                <b-img :src="require('../../static/images/sala2.jpg')"/>
                            </figure>
                            </div>
                            <div class="col-sm-6">
                            <figure>
                                <b-img :src="require('../../static/images/rowerki.jpeg')"/>
                            </figure>
                            </div>
                        </div>
                    </div>

                    <div class="col-sm-6 d-flex justify-content-center">
                        <div class="row">
                            <b-form id="loginForm">
                            <div class="form-group row">
                                <label for="login-input">Login</label>
                                <b-form-input type="text" v-model="login" class="form-control" id="login-input" aria-describedby="emailHelp" placeholder="Wprowadź login"/>
                            </div>
                            <div class="form-group row">
                                <label for="pass-input">Hasło</label>
                                <b-form-input type="password" v-model="password" class="form-control" id="pass-input" placeholder="Wprowadź hasło"/>
                            </div>
                            <div class="form-group row">
                                <div class="col-md-4 offset-md-7">
                                <b-button @click="onSubmit" class="btn btn-primary">Zaloguj</b-button>
                                </div>
                            </div>
                            </b-form>
                        </div>
                    </div>
                </div>
            </section>
    </div>
</template>

<script>
import NavBar from '../components/NavBar.vue'
import axios from 'axios'

export default {
    components: { NavBar },
    name: "Login",
    data() {
        return {
            login: '',
            password: ''
        }
    },
    methods: {
        async onSubmit() {
            const token = `${this.login}:${this.password}`;
            const encodedToken = Buffer.from(token).toString('base64');
            const session_url = 'http://130.61.111.97:20001/login';

            var config = {
                method: 'get',
                url: session_url,
                headers: { 'Authorization': 'Basic '+ encodedToken }
            };

            axios(config)
            .then(response => {
                console.log(response.data)
                //localStorage.setItem('token', response.data.token)
                this.$router.push('/currentClients')
            })
            .catch(function (error) {
                console.log(error);
            });
            // let result = axios.get(
            //     'http://130.61.111.97:20001/login?login=${this.login}&password=${this.password}'
            // )
            // console.warn(result)

            // if(result.status == 201 && result.data.length > 0) {
            //     //this.$router.push({name: "CurrentClients"})
            // }
        }
    }
}
</script>

<style>
.photos {
    height: 100%;
}
.photos img
{
    width: 100%;
	height: auto;
}
#loginForm
{
    margin-top: 50px;
}
h2 {
    margin-top: 5px;
}
</style>