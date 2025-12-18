import { StyledContainer } from "./home.styles";
import type { HomeComponent } from "./home.types";
import QueryForm from "../../features/query/components/QueryForm/QueryForm";
import Header from "../../layouts/Header/Header";
import { Stack, Typography } from "@mui/material";

const Home: HomeComponent = () => {
    return (
        <StyledContainer>
            <Header/>
            <Stack className="body">
                <Typography variant="h6">Éditeur de texte malagasy</Typography>
                <QueryForm/>
            </Stack>
        </StyledContainer>
    )
}

export default Home