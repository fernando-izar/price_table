import { Layout } from "antd";
import { Header, Footer, Content } from "antd/lib/layout/layout";
import { Products } from "./components/Products";
import "./App.css";

function App() {
  return (
    <Layout className="app-layout">
      <Header className="app-header">
        <Content className="app-header-content">React-test</Content>
      </Header>
      <Layout>
        <Content className="content-layout">
          <Products />
        </Content>
      </Layout>
      <Footer className="app-footer">
        <Content className="app-footer-content">
          by Fernando Cristante Izar
        </Content>
      </Footer>
    </Layout>
  );
}

export default App;
