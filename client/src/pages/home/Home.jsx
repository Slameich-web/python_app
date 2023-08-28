import React from "react";
import { useEffect, useState } from "react";
import { $api } from "../../http/index";
import MenuIcon from "@mui/icons-material/Menu";
import CloseIcon from "@mui/icons-material/Close";
import { useTransition } from "@react-spring/web";
import { animated } from "@react-spring/web";
import { Link } from "react-router-dom";

export const Home = () => {
  const getUser = async () => {
    try {
      await $api.get("/api/user");
    } catch (e) {
      console.log(e.response.data.message);
    }
  };
  useEffect(() => {
    getUser();
  });
  const [showNavbar, setShowNavbar] = useState(false);
  const transition = useTransition(showNavbar, {
    from: { x: -100, y: 100, opacity: 0 },
    enter: { x: 0, y: 0, opacity: 1 },
    leave: { x: 100, y: 100, opacity: 0 },
  });
  return (
    <div className="auth_wrapper">
      <div className="nav_container">
        <div className="drop_down">
          <div
            className="drop_down_button"
            onClick={() => setShowNavbar((prev) => !prev)}
          >
            {showNavbar ? (
              <CloseIcon fontSize="large" />
            ) : (
              <MenuIcon fontSize="large" />
            )}
          </div>
        </div>
        {transition((style, item) =>
          item ? (
            <animated.div style={style} className="buttons">
              <Link
                to={"/revenue"}
                style={{
                  width: "100%",
                  height: "100%",
                  display: "flex",
                  justifyContent: "center",
                  textDecoration: "none",
                  color: "var(--tg-theme-button-text-color)",
                }}
              >
                <animated.button style={style}>Доход</animated.button>
              </Link>
              <Link
                to={"/checkouts"}
                style={{
                  width: "100%",
                  height: "100%",
                  display: "flex",
                  justifyContent: "center",
                  textDecoration: "none",
                  color: "var(--tg-theme-button-text-color)",
                }}
              >
                <animated.button style={style}>
                  Запросить выплату
                </animated.button>
              </Link>
            </animated.div>
          ) : (
            ""
          )
        )}
      </div>
    </div>
  );
};
