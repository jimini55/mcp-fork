# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions
# and limitations under the License.
"""Tests for the frontend MCP Server."""

import pytest
from awslabs.frontend_mcp_server.server import (
    base_user_interface_web_app,
    optimistic_ui,
    using_amplify_authenticator,
)
from awslabs.frontend_mcp_server.static import (
    OPTIMISTIC_UI,
    SETUP_INSTRUCTIONS,
    USING_AMPLIFY_AUTHENTICATOR,
)
from unittest.mock import MagicMock


@pytest.mark.asyncio
async def test_base_user_interface_web_app():
    """Test the base_user_interface_web_app tool returns correct setup instructions."""
    # Arrange
    test_query = 'How do I set up a React app?'
    mock_ctx = MagicMock()

    # Act
    result = await base_user_interface_web_app(test_query, mock_ctx)

    # Assert
    assert result == SETUP_INSTRUCTIONS


@pytest.mark.asyncio
async def test_optimistic_ui():
    """Test the optimistic_ui tool returns correct optimistic UI implementation guide."""
    # Arrange
    test_query = 'How do I implement optimistic UI?'
    mock_ctx = MagicMock()

    # Act
    result = await optimistic_ui(test_query, mock_ctx)

    # Assert
    assert result == OPTIMISTIC_UI


@pytest.mark.asyncio
async def test_using_amplify_authenticator():
    """Test the using_amplify_authenticator tool returns correct authentication guide."""
    # Arrange
    test_query = 'How do I use the Amplify Authenticator?'
    mock_ctx = MagicMock()

    # Act
    result = await using_amplify_authenticator(test_query, mock_ctx)

    # Assert
    assert result == USING_AMPLIFY_AUTHENTICATOR
