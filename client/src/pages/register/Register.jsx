import React, { useState, useEffect } from "react";
import axios from "axios";
import "../../App.scss";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [isRedirect, setIsEedirect] = useState(false);
  const isShowPassword = showPassword ? "text" : "password";
  const navigate = useNavigate();

  const registerRequest = async () => {
    try {
      await axios.post("http://127.0.0.1:8000/api/register", {
        email: email,
        password: password,
        telegram_id: 542,
      });
      setIsEedirect(true);
    } catch (e) {
      setError(e.response.data.message);
    }
  };
  useEffect(() => {
    if (isRedirect) {
      return navigate("/login");
    }
  }, [isRedirect, navigate]);

  return (
    <div className="auth_wrapper">
      <div className="auth_container">
        <form
          className="input_container"
          method="POST"
          autoComplete="off"
          action="users/id"
        >
          <input
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
            type="email"
          />
          <input
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Пароль"
            type={isShowPassword}
          />
        </form>
        <div>
          <span>Показать пароль </span>
          <input
            type="checkbox"
            onChange={() => setShowPassword((prev) => !prev)}
          />
        </div>
        <a href="https://ya.ru/">Забыли пароль?</a>
        <button onClick={registerRequest} className="login_button">
          Регистрация
        </button>
        <div>{error}</div>
      </div>
    </div>
  );
};

export default Register;
