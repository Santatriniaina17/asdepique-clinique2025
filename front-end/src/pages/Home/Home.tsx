import { StyledContainer } from "./home.styles";
import type { HomeComponent } from "./home.types";
import QueryForm from "../../features/query/components/QueryForm/QueryForm";

const Home: HomeComponent = () => {
    return (
        <StyledContainer>
            <QueryForm />
        </StyledContainer>
    )
}

export default Home