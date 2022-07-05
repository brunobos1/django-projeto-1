import { useNavigate } from "react-router";
import { useState } from "react";
import { Link } from "react-router-dom";
import { api } from "./Login";

export default function Signup() {
    const navigate = useNavigate();
    const [isPending, setIsPending] = useState(false);
    const [teste, setTest] = useState(false);
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [cpf, setCPF] = useState("");
    const [pis, setPIS] = useState("");
    const [password, setPassword] = useState("");
    const [country, setCountry] = useState("");
    const [region, setRegion] = useState("");
    const [city, setCity] = useState("");
    const [zipcode, setZipcode] = useState("");
    const [street, setStreet] = useState("");
    const [number, setNumber] = useState("");
    const [additional, setAdditional] = useState("");

    const signup = () => {

        if ((email == "") & (password == "")) {
        return;
        } else {

        setIsPending(true);

        api
            .post("/cadastrar", {
            nome: name,
            email: email,
            cpf: cpf,
            pis: pis,
            senha: password,
            pais: country,
            estado: region,
            municipio: city,
            cep: zipcode,
            rua: street,
            numero: number,
            complemento: additional
            })
            .then(function (response) {
            console.log(response.data);

                navigate('/');
                setIsPending(false);
                setTest(true)

            })
            .catch(function (error) {
            console.log(error, "error");
            setIsPending(false);
            });
        }
    };        

    return (
        <>
        <div class="form-container sign-in-container">
            <form>
            <h1>Crie sua conta</h1>
            <div class="social-container">
                <a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
                <a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
                <a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
            </div>
            <span>ou preencha seus dados</span>
                <input type="text" placeholder="Nome" onChange={(e) => setName(e.target.value)}/>
                <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)}/>
                <input type="text" placeholder="CPF" onChange={(e) => setCPF(e.target.value)}/>
                <input type="text" placeholder="PIS" onChange={(e) => setPIS(e.target.value)}/>
                <input type="password" placeholder="Senha" onChange={(e) => setPassword(e.target.value)}/>
                <input type="text" placeholder="País" onChange={(e) => setCountry(e.target.value)}/>
                <input type="text" placeholder="Estado" onChange={(e) => setRegion(e.target.value)}/>
                <input type="text" placeholder="Municipio" onChange={(e) => setCity(e.target.value)}/>
                <input type="text" placeholder="CEP" onChange={(e) => setZipcode(e.target.value)}/>
                <input type="text" placeholder="Rua" onChange={(e) => setStreet(e.target.value)}/>
                <input type="text" placeholder="Número" onChange={(e) => setNumber(e.target.value)}/>
                <input type="text" placeholder="Complemento" onChange={(e) => setAdditional(e.target.value)}/>
            { !isPending && <button type="submit" onClick={signup}>Criar</button>}
            { isPending && <button disabled type="submit">Criando usuário...</button>}
            {teste &&<p></p>}
            </form>
        </div>
        <div class="overlay-container">
                <div class="overlay">
                <div class="overlay-panel overlay-right">
                    <h1>Olá visitante!</h1>
                    <p>Sinta-se a vontade para continuar seu cadastro ou entrar no nosso sistema caso já tenha uma conta</p>
                    <Link to='/'><button class="ghost" id="signUp">Entrar</button></Link>
                </div>
                </div>
            </div>
        </>

    );
}