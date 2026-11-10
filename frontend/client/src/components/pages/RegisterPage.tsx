import RegisterForm from "../forms/RegisterForm"
import { useNavigate } from "react-router-dom"


const RegisterPage = () => {

    let navigate = useNavigate()


    return(
        <>
        <RegisterForm onSuccess={() =>
            navigate('/login')
        }/>
        </>
    )
}

export default RegisterPage