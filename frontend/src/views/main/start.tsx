/* typescript start page */
import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { createBrowserHistory } from "history";
import { createRoot } from "react-dom";
import { App } from "./App";
import { Login } from "./views/Login";
import { PasswordRecovery } from "./views/PasswordRecovery";
import { ResetPassword } from "./views/ResetPassword";
import { Main } from "./views/main/Main";
import { Dashboard } from "./views/main/Dashboard";
import { UserProfile } from "./views/main/profile/UserProfile";
import { UserProfileEdit } from "./views/main/profile/UserProfileEdit";
import { RouterComponent } from "./router";
import { User } from "./views/main/user/User";
import { UserEdit } from "./views/main/user/UserEdit";
import { UserCreate } from "./views/main/user/UserCreate";
import { UserView } from "./views/main/user/UserView";
import { UserList } from "./views/main/user/UserList";
import { Role } from "./views/main/role/Role";
import { RoleEdit } from "./views/main/role/RoleEdit";
import { RoleCreate } from "./views/main/role/RoleCreate";
import { RoleView } from "./views/main/role/RoleView";

const history = createBrowserHistory();
const root = createRoot(document.getElementById("root") as HTMLElement);
root.render(
    <BrowserRouter history={history}>
        <Routes>
            <Route path="/" element={<App />}>
                <Route path="login" element={<Login />} />
                <Route path="recover-password" element={<PasswordRecovery />} />
                <Route path="reset-password" element={<ResetPassword />} />
                <Route path="main" element={<Main />}>
                    <Route path="dashboard" element={<Dashboard />} />
                    <Route path="profile" element={<RouterComponent />}>
                        <Route path="view" element={<UserProfile />} />
                        <Route path="edit" element={<UserProfileEdit />} />
                    </Route>
                    <Route path="user" element={<RouterComponent />}>
                        <Route path="list" element={<UserList />} />
                        <Route path="create" element={<UserCreate />} />
                        <Route path="edit/:id" element={<UserEdit />} />
                        <Route path="view/:id" element={<UserView />} />
                    </Route>
                    <Route path="role" element={<RouterComponent />}>
                        <Route path="list" element={<Role />} />

                        <Route path="create" element={<RoleCreate />} />

                        <Route path="edit/:id" element={<RoleEdit />} />
                        
                        <Route path="view/:id" element={<RoleView />} />
                    </Route>
                </Route>
            </Route>
        </Routes>
    </BrowserRouter>
);

