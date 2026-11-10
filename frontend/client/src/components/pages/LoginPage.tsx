import LoginForm from "../forms/LoginForm"
import { useNavigate } from "react-router-dom"



const LoginPage = () => {

    let navigate = useNavigate()

    return(
        <>
        <LoginForm
            onSuccess={() => {
                navigate('/home')
            }}
        />
        </>
    )
}

export default LoginPage