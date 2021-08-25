<map version="freeplane 1.7.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Demo Mindmap" FOLDED="false" ID="ID_1002858447" CREATED="1629749144699" MODIFIED="1629847684990" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" show_icon_for_attributes="true" show_note_icons="true" fit_to_viewport="false"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="6" RULE="ON_BRANCH_CREATION"/>
<hook NAME="accessories/plugins/AutomaticLayout.properties" VALUE="ALL"/>
<node TEXT="Heading 1" POSITION="right" ID="ID_830578047" CREATED="1629847687835" MODIFIED="1629847817509">
<edge COLOR="#ff0000"/>
<richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      This is text under the heading
    </p>
    <p>
      
    </p>
    <p>
      And formatted with standard markdown.
    </p>
    <p>
      
    </p>
    <p>
      [google](http://www.google.com)
    </p>
    <p>
      ---
    </p>
  </body>
</html>
</richcontent>
</node>
<node TEXT="Heading 1 - children are list" POSITION="right" ID="ID_1233853918" CREATED="1629847817924" MODIFIED="1629848215137">
<edge COLOR="#00ff00"/>
<attribute NAME="child" VALUE="list"/>
<node TEXT="Grace Hopper" ID="ID_1651889194" CREATED="1629847925332" MODIFIED="1629849214268" LINK="grace_hopper.jpg"/>
<node TEXT="This is a url" ID="ID_1238586631" CREATED="1629847951939" MODIFIED="1629847962613" LINK="https://www.google.com"/>
<node TEXT="Level 1 - foo" ID="ID_799619947" CREATED="1629848029644" MODIFIED="1629848099389">
<node TEXT="Level 2 - foo" ID="ID_467686316" CREATED="1629848051380" MODIFIED="1629848061806">
<node TEXT="Level 3 - foo" ID="ID_1156427952" CREATED="1629848044199" MODIFIED="1629848136775"/>
<node TEXT="Level 3 - bar" ID="ID_1256375477" CREATED="1629848044199" MODIFIED="1629848139727"/>
<node TEXT="Level 3 - baz" ID="ID_1150038660" CREATED="1629848044199" MODIFIED="1629848149484"/>
<node TEXT="Grace Hopper" ID="ID_1002357682" CREATED="1629848157579" MODIFIED="1629849181178" LINK="grace_hopper.jpg"/>
</node>
<node TEXT="Level 2 - bar" ID="ID_102851487" CREATED="1629848063065" MODIFIED="1629848066291"/>
<node TEXT="Level 2 - baz" ID="ID_79544560" CREATED="1629848066645" MODIFIED="1629848070561"/>
</node>
<node TEXT="Level 1 - bar" ID="ID_253937581" CREATED="1629848100401" MODIFIED="1629848103676"/>
<node TEXT="Level 1 - baz" ID="ID_1155505516" CREATED="1629848103981" MODIFIED="1629848107019"/>
</node>
<node TEXT="Heading 1 - plain" POSITION="right" ID="ID_1381779178" CREATED="1629848219758" MODIFIED="1629848226688">
<edge COLOR="#ff00ff"/>
<node TEXT="Heading 2" ID="ID_428201527" CREATED="1629848236965" MODIFIED="1629848269137"><richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      This is heading # 2
    </p>
    <p>
      
    </p>
    <p>
      This goes directly below the heading
    </p>
  </body>
</html>
</richcontent>
<node TEXT="Heading 3" ID="ID_1740950284" CREATED="1629848245900" MODIFIED="1629848284270"><richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      This is the context for heading #3
    </p>
  </body>
</html>
</richcontent>
</node>
<node TEXT="Heading 3 - But with children" ID="ID_1160489756" CREATED="1629848289975" MODIFIED="1629848308720">
<attribute NAME="child" VALUE="list"/>
<node TEXT="Level 1 - foo" ID="ID_294185369" CREATED="1629848029644" MODIFIED="1629848099389">
<node TEXT="Level 2 - foo" ID="ID_1037989152" CREATED="1629848051380" MODIFIED="1629848061806">
<node TEXT="Level 3 - foo" ID="ID_1380649576" CREATED="1629848044199" MODIFIED="1629848136775"/>
<node TEXT="Level 3 - bar" ID="ID_824142130" CREATED="1629848044199" MODIFIED="1629848139727"/>
<node TEXT="Level 3 - baz" ID="ID_1196646258" CREATED="1629848044199" MODIFIED="1629848149484"/>
<node TEXT="Grace Again!" ID="ID_20643563" CREATED="1629848157579" MODIFIED="1629849203076" LINK="grace_hopper.jpg"/>
</node>
<node TEXT="Level 2 - bar" ID="ID_341560053" CREATED="1629848063065" MODIFIED="1629848066291"/>
<node TEXT="Level 2 - baz" ID="ID_1780361012" CREATED="1629848066645" MODIFIED="1629848070561"/>
</node>
<node TEXT="Level 1 - bar" ID="ID_607876961" CREATED="1629848100401" MODIFIED="1629848103676"/>
<node TEXT="Level 1 - baz" ID="ID_1597269522" CREATED="1629848103981" MODIFIED="1629848107019"/>
</node>
</node>
<node TEXT="Heading 2 - code snip" ID="ID_1770063503" CREATED="1629848359647" MODIFIED="1629901270304"><richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Bash
    </p>
    <p>
      
    </p>
    <p>
      ```
    </p>
    <p>
      cnt=0
    </p>
    <p>
      while true; do
    </p>
    <p>
      &#160;&#160;&#160;echo &quot;Counting: ${cnt}&quot;
    </p>
    <p>
      &#160;&#160;&#160;cnt=$((cnt + 1))
    </p>
    <p>
      &#160;&#160;&#160;test ${cnt} -gt 1000 &amp;&amp; break
    </p>
    <p>
      done
    </p>
    <p>
      ```
    </p>
  </body>
</html>

</richcontent>
</node>
</node>
</node>
</map>
