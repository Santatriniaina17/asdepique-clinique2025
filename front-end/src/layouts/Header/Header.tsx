import { Box } from "@mui/material";
import { StyledContainer } from "./header.styles";
import type { HeaderComponent } from "./header.types";

const Header: HeaderComponent = () => {
    return (
        <StyledContainer>
            <Box component="img" className="img_ispm" src="/ispm.png"/>
        </StyledContainer>
    )
}

export default Header