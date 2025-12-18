import { StyledContainer } from "./home.styles";
import type { HomeComponent } from "./home.types";
import QueryForm from "../../features/query/components/QueryForm/QueryForm";
import Header from "../../layouts/Header/Header";
import { Stack, Typography } from "@mui/material";
import Input from "../../shared/components/Input/Input";
import ontologyDomain from "../../shared/constants/ontologyDomain";

const Home: HomeComponent = () => {
    return (
        <StyledContainer>
            <Header/>
            <Stack className="body">
                <Typography variant="h6">Éditeur de texte malagasy</Typography>
                <Stack className="form">
                    <QueryForm/>
                    <Input
                        disabled
                        value={ontologyDomain}
                    />
                </Stack>
            </Stack>
        </StyledContainer>
    )
}

export default Home