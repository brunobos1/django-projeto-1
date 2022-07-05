import { useNavigate } from "react-router";
import { useState } from "react";
import { api } from "./Login";
import { cookies } from "./Login";

export default function Profile() {
    const navigate = useNavigate();
    const [teste, setTest] = useState(false);
    const [name, setName] = useState("");
    const [password, setPassword] = useState("");
    const [country, setCountry] = useState("");
    const [region, setRegion] = useState("");
    const [city, setCity] = useState("");
    const [zipcode, setZipcode] = useState("");
    const [street, setStreet] = useState("");
    const [number, setNumber] = useState("");
    const [additional, setAdditional] = useState("");

    var token_r = cookies.get('token')
    var nome_usuario = cookies.get('user')

    const alterar = () => {

        api
            .put("/alterar", {
            nome: name,
            senha: password,
            pais: country,
            estado: region,
            municipio: city,
            cep: zipcode,
            rua: street,
            numero: number,
            complemento: additional
            }, {headers: {Authorization: 'Bearer ' + token_r}})
            .then(function (response) {
            console.log(response.data);
            setTest(true)
            })
            .catch(function (error) {
            console.log(error, "error");
            });
    };

    const deletar = () => {

            api
            .delete("/deletar", {headers: {Authorization: 'Bearer ' + token_r}})
            .then(function (response) {
                console.log(response.data.token, "response.data.token");
                cookies.remove("token");
                cookies.remove("user");
                navigate("/");

            })
            .catch(function (error) {
                console.log(error, "error");

            });
        }

    const signOut = () => {
            cookies.remove("token");
            cookies.remove("user");
            navigate("/");
        };

    

    return (

        <div>
            
            <div class="form-container sign-in-container">
                <form>
                <h1 class="prifile-h1">Alterar dados</h1>
                <input type="text" placeholder="Nome" class="update" onChange={(e) => setName(e.target.value)}/>
                <input type="password" placeholder="Senha" class="update" onChange={(e) => setPassword(e.target.value)}/>
                <input type="text" placeholder="País" class="update" onChange={(e) => setCountry(e.target.value)}/>
                <input type="text" placeholder="Estado" class="update" onChange={(e) => setRegion(e.target.value)}/>
                <input type="text" placeholder="Municipio" class="update" onChange={(e) => setCity(e.target.value)}/>
                <input type="text" placeholder="CEP" class="update" onChange={(e) => setZipcode(e.target.value)}/>
                <input type="text" placeholder="Rua" class="update" onChange={(e) => setStreet(e.target.value)}/>
                <input type="text" placeholder="Número" class="update" onChange={(e) => setNumber(e.target.value)}/>
                <input type="text" placeholder="Complemento" class="update" onChange={(e) => setAdditional(e.target.value)}/>
                <button type="button" class="profile-button" onClick={alterar}>Alterar</button>
                <button type="button" class="profile-button" onClick={deletar}>Deletar conta</button>
                {teste&&<p>Cadastro alterado com sucesso!</p>}
                </form>
                
            </div>
            <div class="overlay-container">
                <div class="overlay">
                <div class="overlay-panel overlay-right">
                    <h1>Olá {nome_usuario}!</h1>
                    <p>Caso queira sair da sua conta por favor clique no botão abaixo</p>
                    <button class="ghost" id="signUp" onClick={signOut}>Sair</button>
                </div>
                </div>
            </div>
            

        </div>

    );
}