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
from awslabs.frontend_mcp_server.server import get_react_docs_by_topic
from unittest.mock import patch


@pytest.mark.asyncio
@patch('awslabs.frontend_mcp_server.server.load_markdown_file')
async def test_get_react_docs_by_topic_essential_knowledge(mock_load_markdown):
    """Test the get_react_docs_by_topic tool returns correct content for essential-knowledge topic."""
    # Arrange
    mock_load_markdown.return_value = 'Essential knowledge content'

    # Act
    result = await get_react_docs_by_topic('essential-knowledge')

    # Assert
    mock_load_markdown.assert_called_once_with('essential-knowledge.md')
    assert result == 'Essential knowledge content'


@pytest.mark.asyncio
@patch('awslabs.frontend_mcp_server.server.load_markdown_file')
async def test_get_react_docs_by_topic_troubleshooting(mock_load_markdown):
    """Test the get_react_docs_by_topic tool returns correct content for troubleshooting topic."""
    # Arrange
    mock_load_markdown.return_value = 'Troubleshooting content'

    # Act
    result = await get_react_docs_by_topic('troubleshooting')

    # Assert
    mock_load_markdown.assert_called_once_with('troubleshooting.md')
    assert result == 'Troubleshooting content'


@pytest.mark.asyncio
@patch('awslabs.frontend_mcp_server.server.load_markdown_file')
async def test_get_react_docs_by_topic_basic_ui(mock_load_markdown):
    """Test the get_react_docs_by_topic tool returns correct content for basic-ui topic."""
    # Arrange
    mock_load_markdown.return_value = 'Basic UI setup content'

    # Act
    result = await get_react_docs_by_topic('basic-ui')

    # Assert
    mock_load_markdown.assert_called_once_with('basic-ui-setup.md')
    assert result == 'Basic UI setup content'


@pytest.mark.asyncio
@patch('awslabs.frontend_mcp_server.server.load_markdown_file')
async def test_get_react_docs_by_topic_authentication(mock_load_markdown):
    """Test the get_react_docs_by_topic tool returns correct content for authentication topic."""
    # Arrange
    mock_load_markdown.return_value = 'Authentication setup content'

    # Act
    result = await get_react_docs_by_topic('authentication')

    # Assert
    mock_load_markdown.assert_called_once_with('authentication-setup.md')
    assert result == 'Authentication setup content'


@pytest.mark.asyncio
@patch('awslabs.frontend_mcp_server.server.load_markdown_file')
async def test_get_react_docs_by_topic_routing(mock_load_markdown):
    """Test the get_react_docs_by_topic tool returns correct content for routing topic."""
    # Arrange
    mock_load_markdown.return_value = 'Routing setup content'

    # Act
    result = await get_react_docs_by_topic('routing')

    # Assert
    mock_load_markdown.assert_called_once_with('routing-setup.md')
    assert result == 'Routing setup content'


@pytest.mark.asyncio
@patch('awslabs.frontend_mcp_server.server.load_markdown_file')
async def test_get_react_docs_by_topic_customizing(mock_load_markdown):
    """Test the get_react_docs_by_topic tool returns correct content for customizing topic."""
    # Arrange
    mock_load_markdown.return_value = 'Amplify theme customization content'

    # Act
    result = await get_react_docs_by_topic('customizing')

    # Assert
    mock_load_markdown.assert_called_once_with('amplify-theme-customization.md')
    assert result == 'Amplify theme customization content'


@pytest.mark.asyncio
@patch('awslabs.frontend_mcp_server.server.load_markdown_file')
async def test_get_react_docs_by_topic_creating_components(mock_load_markdown):
    """Test the get_react_docs_by_topic tool returns correct content for creating-components topic."""
    # Arrange
    mock_load_markdown.return_value = 'Creating components content'

    # Act
    result = await get_react_docs_by_topic('creating-components')

    # Assert
    mock_load_markdown.assert_called_once_with('creating-components.md')
    assert result == 'Creating components content'


@pytest.mark.asyncio
async def test_get_react_docs_by_topic_invalid():
    """Test the get_react_docs_by_topic tool raises ValueError for invalid topic."""
    # Act & Assert
    with pytest.raises(ValueError, match='Invalid topic:'):
        await get_react_docs_by_topic('invalid-topic')
