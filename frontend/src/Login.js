import { useNavigate } from "react-router";
import { fetchToken, setToken } from "./Auth";
import { useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import Cookies from 'universal-cookie';

export const cookies = new Cookies();

export const api = axios.create({
    baseURL: 'https://app1-login-api.herokuapp.com/'
})

export default function Login() {
    
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const login = () => {

        if ((username == "") & (password == "")) {
        return;
        } else {

        api
            .post("/token", {
            login: username,
            senha: password,
            })
            .then(function (response) {
            console.log(response.data.token);
            if (response.data.token) {
                setToken(response.data.token);
                cookies.set('user', response.data.nome_usuario);
                navigate('/profile');
            }
            })
            .catch(function (error) {
            console.log(error, "error");
            });
        }
    };

    return (

      <div>
        {fetchToken() ? (<p>you are logged in</p>) : (

        <div>

            <div class="form-container sign-in-container">
            <form>
                <h1>Login</h1>
                
                <label>
                    <input type="text" placeholder="Email/CPF/PIS" onChange={(e) => setUsername(e.target.value)}/>
                    <input type="password" placeholder="Senha" onChange={(e) => setPassword(e.target.value)}/>
                </label>
              <button type="button" onClick={login}>
                Login
              </button>
            </form>
            </div>
            <div class="overlay-container">
                <div class="overlay">
                <div class="overlay-panel overlay-right">
                    <h1>Olá visitante!</h1>
                    <p>Caso não tenha um conta clique no botão abaixo para se cadastrar</p>
                    <Link to='/signup'><button class="ghost" id="signUp">Cadastrar</button></Link>
                </div>
                </div>
            </div>
        </div>
        )}
      </div>
    );
}