<template>
    <div>
        <NavBar />
        <h2>Klub fitness - klub z zasadami</h2>
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
                            <div v-if="loginError" class="error">{{ loginErrorMsg }}</div>
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
                                <b-button @click="getLogIn" class="btn btn-primary">Zaloguj</b-button>
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

export default {
    components: { NavBar },
    name: "Login",
    data() {
        return {
            login: '',
            password: '',
            loginError: false,
            loginErrorMsg: 'Niepoprawny login lub hasło'
        }
    },
    methods: {
        getLogIn() {
            const token = `${this.login}:${this.password}`;
            const encodedToken = Buffer.from(token).toString('base64');
            var myHeaders = new Headers();
            myHeaders.append("Authorization", "Basic " + encodedToken);

            console.log(process.env.API_URL)

            var requestOptions = {
                method: 'GET',
                headers: myHeaders,
                redirect: 'follow',
                credentials: 'include',
            };

            fetch(process.env.API_URL + "login", requestOptions)
            .then(res => {
                if(res.ok) {
                    this.$router.push('/currentClients')
                }
                else {
                    this.loginError = true
                }
            })
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
.error {
    color: #ff0062;
    margin-bottom: 10px;
    font-size: 0.8em;
    font-weight: bold;
  }
</style>