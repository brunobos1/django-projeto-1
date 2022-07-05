import { useLocation,Navigate } from "react-router-dom"
import Cookies from 'universal-cookie';

const cookies = new Cookies();

export const setToken = (token)=>{

    cookies.set('token', token);

}

export const fetchToken = (token)=>{

    return cookies.get('token')
}

export function RequireToken({children}){

    let auth = fetchToken()
    let location = useLocation()

    if(!auth){

        return <Navigate to='/' state ={{from : location}}/>;
    }

    return children;
}