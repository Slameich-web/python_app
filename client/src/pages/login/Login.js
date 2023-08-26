import React, { useState } from "react";
import axios from "axios";
import "../../App.scss";

const Login = () => {
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const isShowPassword = showPassword ? "text" : "password";

  const loginRequest = async () => {
    try {
      await axios.post("http://127.0.0.1:8000/api/login", {
        email: email,
        password: password,
      });
    } catch (e) {
      setError(e.response.data.message);
    }
  };

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
        <button onClick={loginRequest} className="login_button">
          Войти
        </button>
        <div>{error}</div>
      </div>
    </div>
  );
};

export default Login;
